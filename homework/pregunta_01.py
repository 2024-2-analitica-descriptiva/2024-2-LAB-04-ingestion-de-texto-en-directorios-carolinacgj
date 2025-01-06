# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_02():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
import os
import zipfile
import csv

def pregunta_01():
    # Rutas de los archivos
    zip_path = "files/input.zip"
    input_dir = "input"
    output_dir = "output"
    train_csv = os.path.join(output_dir, "train_dataset.csv")
    test_csv = os.path.join(output_dir, "test_dataset.csv")

    # Crear carpeta de salida si no existe
    os.makedirs(output_dir, exist_ok=True)

    # Descomprimir el archivo ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall()

    def process_folder(folder_path, output_csv):
        """
        Procesa una carpeta para generar un archivo CSV.

        Args:
            folder_path (str): Ruta de la carpeta (train o test).
            output_csv (str): Ruta del archivo CSV de salida.
        """
        rows = []

        # Recorrer subcarpetas (negative, positive, neutral)
        for sentiment in os.listdir(folder_path):
            sentiment_path = os.path.join(folder_path, sentiment)

            if os.path.isdir(sentiment_path):
                for file_name in os.listdir(sentiment_path):
                    file_path = os.path.join(sentiment_path, file_name)

                    # Leer el contenido del archivo de texto
                    with open(file_path, "r", encoding="utf-8") as file:
                        phrase = file.read().strip()

                    # Añadir fila al CSV
                    rows.append({"phrase": phrase, "sentiment": sentiment})

        # Escribir el archivo CSV
        with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["phrase", "sentiment"])
            writer.writeheader()
            writer.writerows(rows)

    # Procesar las carpetas train y test
    process_folder(os.path.join(input_dir, "train"), train_csv)
    process_folder(os.path.join(input_dir, "test"), test_csv)

# Llamar a la función
pregunta_01()

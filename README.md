# Detector de Bocha

Este é um projeto que utiliza a biblioteca OpenCV em Python para manipulação de imagem para encontrar os círculos. Neste trabalho, irei demonstrar como realizar a captura dos círculos utilizando o threshold e também o filtro canny.

## Sobre o trabalho

- Disciplina: OP63I-CC8 - Processamento de Imagens e Reconhecimento de Padrões
- Turma: 2023/2 - 8° Período
- Professor: Pedro Luiz de Paula Filho

## Pré-requisitos e Instalação no Linux

### Python (versão recomendada: 3.11 ou superior)

A maioria das distribuições Linux já vem com o Python instalado. Para verificar se o Python está instalado, abra o terminal e digite:

`python3 --version`

Se não estiver instalado, você pode instalá-lo usando o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu/Debian:

`
sudo apt-get update
sudo apt-get install python3
`

No Arch Linux:

`
sudo pacman -Sy python
`

### PyCharm (ou qualquer outra IDE de sua escolha)

Você pode baixar o PyCharm diretamente do site oficial da JetBrains (https://www.jetbrains.com/pycharm/download/) ou, se preferir, pode usar o gerenciador de pacotes da sua distribuição para instalar a versão Community:

#### Ubuntu/Debian:

`
sudo snap install pycharm-community --classic
`

#### Arch Linux:

`
sudo pacman -Sy pycharm-community
`

### OpenCV

Você pode instalar o OpenCV via pip, o gerenciador de pacotes Python:

`
pip install opencv-python
`

### NumPy

NumPy é uma biblioteca amplamente usada para computação numérica em Python. Você pode instalá-lo via pip:

`
pip install numpy
`

## Pré-requisitos e Instalação no Windows

### Python (versão recomendada: 3.11 ou superior)

1. Baixe o instalador Python para Windows no site oficial (https://www.python.org/downloads/windows/).

2. Execute o instalador e marque a opção "Adicionar o Python X.Y ao PATH" durante a instalação, onde X.Y é a versão do Python (por exemplo, 3.11).

### PyCharm (ou qualquer outra IDE de sua escolha)

1. Baixe o instalador do PyCharm Community ou Professional do site oficial da JetBrains (https://www.jetbrains.com/pycharm/download/).

2. Execute o instalador e siga as instruções na tela.

### OpenCV

Você pode instalar o OpenCV via pip, o gerenciador de pacotes de pacotes Python:

Abra o prompt de comando (cmd) e execute:

`
pip install opencv-python
`

### NumPy

NumPy é uma biblioteca amplamente usada para computação numérica em Python. Você pode instalá-lo via pip:

`
pip install numpy
`

## Executando o Projeto

1. Clone este repositório em seu sistema:

`
git clone https://github.com/seuusuario/python-opencv-trabalho.git
`

2. Abra o projeto no PyCharm (ou sua IDE preferida).

## Modo de Uso

![Screenshot_20230909_193426](https://github.com/emanuelamaral/bocha_detector/assets/105809178/a5cac62c-d237-4f9d-bfa9-227b0fc89582)

![Screenshot_20230909_193559](https://github.com/emanuelamaral/bocha_detector/assets/105809178/d99c273d-01ce-4eac-b7a4-df276548519c)

1. **Aplicação de Filtros:**

   - Utilize as trackbars para ajustar o filtro de binarização e também para o filtro Canny.
     
2. **Sair do Programa:** Pressione a tecla `q` para sair do programa.

## Autores

- Amoz Emanuel

## Referências

- [OpenCV Documentation](https://docs.opencv.org/)
- [Python.org](https://www.python.org/)
- [PyCharm](https://www.jetbrains.com/pycharm/)

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

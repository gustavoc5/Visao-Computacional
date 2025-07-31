# Reconhecimento de Emoções Faciais em Tempo Real com CNNs e Transformers

Este projeto tem como objetivo detectar emoções faciais em tempo real a partir da webcam, utilizando modelos de aprendizado profundo como **Mini-Xception** e **Swin Transformer**. A aplicação também integra o reconhecimento ao controle de um jogo simples, alterando comportamentos com base na emoção do usuário.

Desenvolvido como parte do projeto final da disciplina de Visão Computacional da UNIFEI (2025).

---

## 🎯 Objetivos

- Detectar rostos em tempo real com OpenCV (Haar Cascade).
- Classificar emoções faciais utilizando CNNs (Mini-Xception) e Transformers (Swin Transformer).
- Comparar desempenho entre as arquiteturas.
- Controlar elementos de um jogo com base na emoção reconhecida.

---

## 📊 Resultados Obtidos

- **Mini-Xception (FER2013):** ~65% de acurácia.
- **Swin Transformer (FER2013+):** ~23% após fine-tuning.
- Mini-Xception se mostrou mais eficiente para aplicações em tempo real com restrição de hardware.

---

## 📸 Exemplos de Execução

### Emoções Detectadas
![exemplo de emoções](images/demo_emotion.png)

### Controle de jogo com emoção facial
![exemplo do jogo](images/game_demo.png)

---

## ▶️ Como Executar

### Requisitos
- Python 3.8+
- OpenCV
- TensorFlow / Keras
- PyTorch (para o Swin Transformer)

### Rodar a demo em tempo real:
```bash
python3 video_emotion_demo.py

Este repositório é uma adaptação baseada em oarriaga/face_classification, com modificações e extensões desenvolvidas para fins acadêmicos e aplicação prática.

import matplotlib.pyplot as plt
import pandas as pd

# 파일에서 데이터 읽어오기
file_path = 'history.log'  # 파일 경로에 맞게 변경해주세요
data = pd.read_csv(file_path)

# 데이터 시각화
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(data['epoch'], data['accuracy'], label='Accuracy')
plt.plot(data['epoch'], data['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(data['epoch'], data['loss'], label='Loss')
plt.plot(data['epoch'], data['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()

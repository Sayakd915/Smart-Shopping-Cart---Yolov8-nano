from ultralytics import YOLO

model = YOLO('best.pt')

results = model.predict('C://Users//SAYAK DAS//OneDrive//Desktop//Metrics//test_image.jpg')
results[0].show()
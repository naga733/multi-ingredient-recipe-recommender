# Personalized Recipe Recommendation System with Multi-Ingredient Detection using YOLO

**NextMeal** is a web app that recommends recipes based on what's in your kitchen. It uses YOLOv11, a modern object detection model, to identify multiple ingredients from a single image. Once it knows what foods are in the image, it sends that list to a recommendation system that pulls matching recipes from the Soonacular API. The app also takes into account personal preferences like cuisine type, dietary restrictions, and food intolerances to make the suggestions more relevant.

The system has been implemented as an interactive web application, allowing 
users to: 

- Upload images of available ingredients. 

- Specify dietary and culinary preferences.
  
- Manually include and exclude certain ingredients, specify meal types.

- Retrieve personalized recipe suggestions displayed in an intuitive, user
friendly interface. 

---

## Impact

This project addresses critical challenges in food technology, including:  
- **Reducing food wastage** by suggesting recipes for ingredients nearing expiration.  
- **Promoting healthier dietary habits** through personalization.  

It also demonstrates the practical applications of **artificial intelligence in everyday life**, showcasing how advanced detection models like YOLO can be integrated with API-driven services to create impactful solutions.

---

## Tech Stack

**Framework:** Django

**Object Detection:** YOLOv11

**API:** Spoonacular API

**Languages:** Python, HTML, CSS, JavaScript

**Database:** SQLite

---

## Demo Screenshots

### Home Page

<img width="1912" height="861" alt="Home page" src="https://github.com/user-attachments/assets/09f10950-3949-4b91-8c35-82eede0ffcaf" />



### Preferences Page (Account Page)

<img width="1913" height="859" alt="User preferences" src="https://github.com/user-attachments/assets/f22d797f-caf0-4c3e-8df7-33cf03d3894e" />



### Search Recipes Page

<img width="1910" height="856" alt="Search Recipes Page" src="https://github.com/user-attachments/assets/595d45a4-1d69-446f-9617-d44bbba9ce46" />



### Recipe Results Page

<img width="1919" height="861" alt="Recipes" src="https://github.com/user-attachments/assets/0cce9b2b-d41d-48bf-9c84-5c7c7fcb16c5" />



### Detected Ingredients Page

<img width="1916" height="856" alt="Detected ingredients" src="https://github.com/user-attachments/assets/2ab995e2-4c6d-4a57-b563-349659cbca35" />

---

## Dataset Challenges and Improving Model performance

Finding a large dataset for detecting multiple food ingredients in a single image was a tough challenge. The biggest problem was the lack of pre-labeled data, and food images are very tricky - they vary widely in lighting, angles, and often have ingredients overlapping or even partially obscured. 

To address this, I applied a few techniques to boost the model's performance. By using label correction, targeted oversampling, mosaic augmentation and fine-tuning. I was able to improve the macro recall from around 60% to 70%. The biggest improvements came with classes that were underrepresented in the dataset, like the carrot, where the model was previously struggling.

---
## Future Enhancements

- Expand ingredient classes for wider coverage.

- Integrate IoT-enabled smart kitchen devices.

- Implement autonomous recipe generation.

---

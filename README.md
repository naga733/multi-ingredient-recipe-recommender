# Personalized Recipe Recommendation System with Multi-Ingredient Detection using YOLO

**NextMeal** is a web application that provides personalized recipe recommendations by seamlessly integrating multi-ingredient detection with intelligent recipe retrieval. The core innovation lies in leveraging **YOLOv11**, a state-of-the-art object detection model, to accurately identify multiple food ingredients from a single image. The detected ingredients are then passed to a dynamic recommendation module, which retrieves tailored recipes from the Spoonacular API while considering user preferences such as cuisine type, dietary restrictions, and intolerances.

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

## Future Enhancements

- Expand ingredient classes for wider coverage.

- Integrate IoT-enabled smart kitchen devices.

- Implement autonomous recipe generation.

---

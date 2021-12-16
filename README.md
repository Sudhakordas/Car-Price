# Car-Price-Prediction using machine learning
## Index
[Introduction](#introduction)

[Demo](#demo)

[Workflow](#workflow)

[Deployment](#deployment)

[Installation](#installation)


## Introduction
This is completly a end to end machine learning project. Where i trained various machine learning algorithms with the car predictions dataset from kaggle to predict the dataset.
Then choose the best algorithm interms of mean-squared-error. Then convert this project into a web app by using  Flask and html. Finall deploy it into heroku platfrom.

## Demo
Link of the web app: [https://car-ml-app.herokuapp.com/](https://car-ml-app.herokuapp.com/)

![img-1](https://github.com/Sudhakordas/Car-Price/blob/main/Car-Price/Car-1.JPG)
![img-2](https://github.com/Sudhakordas/Car-Price/blob/main/Car-Price/Car-2.JPG)

## Workflow
1. After collecting the data handled missing values and drop the unnecessary columns.  
2. Analyse the data with help of some data visualization tools like matplotlib, sklearn to draw some insight from the data.
3. Apply some feature engineering technique(get the dummy values).
4. Apply various machine learning algorithms and selected the best one with less error and the tuned it.
5. Used  basic html to make the fronted and Flask to make the backend.
6. Finally deployed it in thte heroku platfrom.

## Deployment

Deploy the model according to the instruction of heroku. here is the [link](https://dashboard.heroku.com/apps/car-ml-app/deploy/github) of deploying the web app using github.

## Installation

Here is the way of running it in your system.
## How to run this project in your system.
1. Download or clone the repository
```python
git clone https://github.com/Sudhakordas/Car-Price.git
```
2. Create a new environment.
3. Activate that environment 
 ```python
conda activate environment_name
```
4. Install all the denpendencies.
```python
pip install  -r requirements.txt
```
5. Now run the project.
 ### To run the web app.
 Go to the directory where you have clone the repository.
 Type 
 ```python
 python app.py
```





# Densenet_image_classifier
Classification of images using pretrained Densenet121
### Steps to Install and run API ###
- open terminal and install the following libraries
  keras, tensorflow, numpy, fastapi, pillow and hypercorn-
- To start the API run the following command
  'hypercorn main:app --reload'
- Place the images to test in resources folder.
- API should be up and running in 8000 port
- Verify the same by visiting http://127.0.0.1:8000/docs

### API details ###
- swagger documentation is available at http://127.0.0.1:8000/docs

Examples: 

POST : curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "image_path": "dog.jpg"
}'

Response: 
{
  "response": "Brittany_spaniel"
}

#### Response Codes: ####
200 - Successful

400 - Invalid input

404 - Invalid image

500 - Server Error


### Project Structure ###
/scripts ... contains .py files

/tests ... contains unittests

/resources ... contains the assets used

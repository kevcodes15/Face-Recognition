import face_recognition
from PIL import Image, ImageDraw


#encoding the face of bill gates
image_of_mark = face_recognition.load_image_file('./img/known/mark wahl.jpg')
mark_face_encoding = face_recognition.face_encodings(image_of_mark)[0]

#encoding the face of steve jobs
image_of_steve = face_recognition.load_image_file('./img/known/Steve Jobs.jpg')
steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]

#encoding the face of elon musk
image_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]


#  Create arrays of encodings and names
known_face_encodings = [
  mark_face_encoding,
  steve_face_encoding,
  bill_face_encoding
]

known_face_names = [
  "Mark Wahlberg",
  "Steve Jobs",
  "Bill Gates"
]

# Load test image to find faces in
test_image = face_recognition.load_image_file('./img/unknown/marknsteve.jpg')

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
#Encoding the faces found in the image
face_encodings = face_recognition.face_encodings(test_image, face_locations)
pil_image = Image.fromarray(test_image)

draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
  matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

  name = "Unknown Person"

  # If match
  if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]
  
  # Draw box
  draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

  # Draw label
  text_width, text_height = draw.textsize(name)
  draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
  draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

del draw

# Display image
pil_image.show()


# Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
         name = "Unknown Person"

  # If match
         if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                face_image = test_image[top:bottom, left:right]
                pil_image = Image.fromarray(face_image)
                
# Display image
                pil_image.show()




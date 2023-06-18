# Face-Recognition
Face Recognition and Identification using CNN and Python

-Import the necessary libraries: face_recognition, PIL, and ImageDraw.

-Load and encode the face images of known individuals (Bill Gates, Steve Jobs, Mark Wahlberg) using their respective image files.

-Create arrays to store the known face encodings and names.

-Load the test image in which faces need to be recognized.

-Find the face locations in the test image using face_recognition.face_locations().

-Encode the faces found in the test image using face_recognition.face_encodings().

-Create a pil_image object from the test image for drawing purposes.

-Iterate through the face locations and encodings using zip(face_locations, face_encodings).

-Compare the face encodings with the known face encodings using face_recognition.compare_faces().

-If a match is found, assign the corresponding known face name to the current face.

-Draw a rectangle around the face using ImageDraw.rectangle().

-Draw a label below the face rectangle with the recognized name using ImageDraw.text().

-Repeat the above steps for each face in the test image.

-Display the final annotated image using pil_image.show().

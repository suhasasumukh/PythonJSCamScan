try:
  filename = take_photo('photo.jpg')
  print('Saved to {}'.format(filename))
  
  display(Image(filename))
except Exception as err:
  print(str(err))

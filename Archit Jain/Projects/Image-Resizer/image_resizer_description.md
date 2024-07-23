# Image Resizer

## Project Overview

Image Resizer is a Python script that allows users to resize an image to specified dimensions using the OpenCV library.

The script reads an image, displays it, prompts the user for the new dimensions, resizes the image accordingly, displays the resized image, and then saves the resized image to a file.

## Prerequisites

- Python 3
- OpenCV library

## Installation

1. **Install OpenCV**

   On Arch-based Linux distributions (such as Garuda Linux), you can install OpenCV using the following command:
   ```
   sudo pacman -S python-opencv
   ```

2. **Clone the Repository**

   Clone this repository to your local machine.

3. **Navigate to the Project Directory**

## How to Run

1. **Open a Terminal**

   Open a terminal and navigate to the project directory.

2. **Run the Script**

   Execute the script using Python:
   ```
   python image_resizer.py
   ```

3. **Follow Prompts**

   - The script will display the original image.
   - Enter the new length and width for the image when prompted.
   - The script will then display the resized image and save it as `resized_image.png` in the same directory.

## Code Explanation

Here is a detailed explanation of the code used in the image resizer script:

```python
import cv2
```
- **`cv2`**: This is the OpenCV library. It provides tools for image processing and computer vision tasks.

```python
image = cv2.imread('old_image.png')
```
- This line reads the image file `old_image.png` into the variable `image`.

```python
cv2.imshow("old_image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- **`cv2.imshow("old_image", image)`**: Displays the original image in a window titled "old_image".
- **`cv2.waitKey(0)`**: Waits for any key press to proceed.
- **`cv2.destroyAllWindows()`**: Closes all OpenCV windows.

```python
length = int(input("Enter the length of new image: "))
width = int(input("Enter the width of new image: "))
```
- Prompts the user to enter the desired length and width for the new image and stores these values as integers in the variables `length` and `width`.

```python
new_image = cv2.resize(image, (width, length))
```
- **`cv2.resize(image, (width, length))`**: Resizes the original image to the specified width and length, storing the result in `new_image`.

```python
cv2.imshow("Resized Image", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- **`cv2.imshow("Resized Image", new_image)`**: Displays the resized image in a window titled "Resized Image".
- **`cv2.waitKey(0)`**: Waits for any key press to proceed.
- **`cv2.destroyAllWindows()`**: Closes all OpenCV windows.

```python
cv2.imwrite('resized_image.png', new_image)
```
- **`cv2.imwrite('resized_image.png', new_image)`**: Saves the resized image to a file named `resized_image.png` in the same directory.

## Conclusion

This Image Resizer project demonstrates how to use Python and OpenCV to read, display, resize, and save images.

It covers basic input/output operations, user input handling, and image processing tasks using the OpenCV library.

---


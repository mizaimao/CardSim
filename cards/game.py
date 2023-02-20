"""Main game entry-point."""
import numpy as np
import cv2


FRAME_WIDTH: int = 1280
FRAME_HEIGHT: int = 800
WINDOW_NAME: str = "Chicken"

test_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

def game():
    """Entry-point."""
    key: int = ord('n')
    color_index: int = 0
    while key == ord('n'):
        
        if color_index == len(test_colors):
            color_index = 0
        image: np.ndarray = np.full(
            (FRAME_HEIGHT, FRAME_WIDTH, 3), test_colors[color_index], dtype=np.uint8
        )
        cv2.imshow(WINDOW_NAME, image)

        key = cv2.waitKey(0)
        color_index += 1

        
    cv2.destroyAllWindows()


if __name__ == "__main__":
    """Main function."""
    game()
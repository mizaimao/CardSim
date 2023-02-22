"""Main game entry-point."""
import numpy as np
import cv2

from cards.visual.visual_manger import VisualManager


FRAME_WIDTH: int = 1280
FRAME_HEIGHT: int = 800
WINDOW_NAME: str = "Chicken"



def game():
    """Entry-point."""

    vman: VisualManager = VisualManager(
        frame_width=FRAME_WIDTH, frame_height=FRAME_HEIGHT, color_format="BGR"
    )


    key: int = ord('n')
    
    while key == ord('n'):
        image: np.ndarray = vman.get_frame()
        cv2.imshow(WINDOW_NAME, image)

        key = cv2.waitKey(0)
                
    cv2.destroyAllWindows()


if __name__ == "__main__":
    """Main function."""
    game()
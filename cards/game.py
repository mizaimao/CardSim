"""Main game entry-point."""
import numpy as np
import cv2

from cards.objects.card_table import CardTable


FRAME_WIDTH: int = 1280
FRAME_HEIGHT: int = 800
WINDOW_NAME: str = "Chicken"



def game():
    """Entry-point."""

    card_table: CardTable = CardTable(
        frame_width=FRAME_WIDTH, frame_height=FRAME_HEIGHT, color_format="BGR"
    )

    key: int = ord('n')
    
    while key == ord('n'):
        
        image: np.ndarray = card_table.iter_image()
        cv2.imshow(WINDOW_NAME, image)

        key = cv2.waitKey(0)
                
    cv2.destroyAllWindows()


if __name__ == "__main__":
    """Main function."""
    game()
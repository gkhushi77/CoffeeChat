import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create the flowchart figure
fig, ax = plt.subplots(figsize=(8, 10))
ax.axis("off")

# Helper functions to create shapes and text
def add_parallelogram(x, y, text):
    ax.add_patch(patches.Polygon([[x, y], [x + 2, y + 0.5], [x + 2, y - 0.5], [x, y - 1]],
                                  closed=True, edgecolor='black', facecolor='lightblue'))
    ax.text(x + 1, y - 0.5, text, ha="center", va="center", fontsize=10)

def add_rectangle(x, y, text):
    ax.add_patch(patches.Rectangle((x, y - 0.5), 2, 1, edgecolor='black', facecolor='lightgreen'))
    ax.text(x + 1, y, text, ha="center", va="center", fontsize=10)

def add_diamond(x, y, text):
    ax.add_patch(patches.Polygon([[x, y], [x + 1, y + 1], [x + 2, y], [x + 1, y - 1]],
                                  closed=True, edgecolor='black', facecolor='lightyellow'))
    ax.text(x + 1, y, text, ha="center", va="center", fontsize=10)

def add_arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(facecolor="black", arrowstyle="->"))

# Start
add_parallelogram(4, 14, "Start")

# Input video feed
add_rectangle(4, 12, "Capture Video Feed")
add_arrow(5, 13, 5, 12.5)

# Process frame
add_rectangle(4, 10, "Process Frame with OpenCV")
add_arrow(5, 11, 5, 10.5)

# Hand detection
add_rectangle(4, 8, "Detect Hand using MediaPipe")
add_arrow(5, 9, 5, 8.5)

# Decision: Hand detected?
add_diamond(4, 6, "Hand Detected?")
add_arrow(5, 7, 5, 6.5)

# If yes, find gesture
add_rectangle(8, 6, "Recognize Gesture")
add_arrow(6, 6, 7, 6)

# Perform action
add_rectangle(8, 4, "Perform Action (e.g., Move Mouse, Click)")
add_arrow(9, 5, 9, 4.5)

# Loop back
add_arrow(9, 4, 5, 4)
add_arrow(5, 4, 5, 5.5)

# If no, continue capturing video
add_arrow(5, 5, 5, 4.5)

# End condition
add_diamond(4, 2, "Quit?")
add_arrow(5, 3, 5, 2.5)

# If yes, End
add_parallelogram(4, 0, "End")
add_arrow(5, 1, 5, 0.5)

# Save the flowchart
file_path = "/mnt/data/GestureTrack_Flowchart.png"
plt.savefig(file_path, bbox_inches="tight")
plt.close(fig)

file_path

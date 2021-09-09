_**IMPORTANT**: This folder contains an old, independent project I completed at the beginning of the pandemic during Zoom High School. I was relatively new to Python, and there are plenty of issues in the code. The biggest one is my use of `except: pass`. Regardless, this was the first time I tried using a library without being taught it or following a YouTube tutorial. It was my first experience learning the most important skill any programmer can develop: the art of Googling. It really isn't much, but looking back, I'm incredibly proud of what I was able to learn from this experience. Plus, the end result is pretty fun.<br /> Enjoy!_

Summary:

A few months ago, I started trying to generate fractals in Python. Most notably, I created a function that recursively generated the Sierpinski Triangle. Once I did this, I realized that this was a great way to learn more about the applications of recursive functions while creating fun pieces of art. With this in mind, I chose this project.

This project aims to focus on two major aspects: algorithm design and UI/UX. The algorithm design comes into play with the fractal tree generator. While one layer of difficulty comes with creating a function to recursively generate trees, I added an additional layer of difficulty by requiring a large range of possible outputs through 10 inputs.

While the fractal tree generator is easy to use, a seamless user experience can make it even more enjoyable, which is why I created a GUI for this project as well. I took inspiration from PhET simulations, giving the user free range to alter the inputs however they like—within reason.

tree.py:

The entirety of the usable part of tree.py is the Tree class. The Tree class takes 10 inputs as ways to modify the generated fractal tree. In some cases, like with the number of splitting branches, these inputs can be used very directly with little modification. Other inputs, like the number of layers, require some simple algebra to become usable by the rest of the program.

These discrepancies occur because the trees are generated recursively. Since they’re recursive, counting the number of layers is much more difficult, so these kinds of inputs are converted into pixel amounts and become the terminating conditions for the recursive function.

While the user could input these pixel lengths, these are arbitrary, as the user doesn’t know how they are going to work together. Through this method, the user can better understand how each of their inputs is working to modify the tree.

In order to actually draw the tree, I use Turtle graphics. Since Turtle generates graphics by drawing straight lines and turning, this gives me full control over tree generation, as these are the inputs I would give to any graphics module anyways.

Through the create and _create methods, the Turtle generates the tree. The create method is non-recursive and merely serves to initiate generation. The _create method is a recursive method with a complexity of O(2n). While this does seem slow, this is necessary because the number of branches has exponential asymptotic behaviour. The _create method moves forward to generate a tree, uses a for-loop to recursively call itself multiple times to generate more trees at the top, and returns back to its initial position. The method won’t generate more trees if the length of the new branch is too small.

Finally, after the tree has been generated, the user has the option to save the image. On most machines, the saved postscript file will open as a PDF.

main.py:

This portion both contains and runs the GUI. The GUI utilizes tkinter in an effort to use libraries that come pre-installed with Python. With such a simple design, I focused on keeping the system clean and mostly bug-free rather than adding too many features.

On the only page of the GUI, there are 10 inputs available to the user: seven sliders and three text fields. Many of the sliders are dependent on one another, limiting and expanding their range as others change. This serves two functions. One, this creates limits that provide great freedom to the user while still keeping generating time short. Two, this eliminates any redundant inputs.

Since text fields have a large range of inputs, if the colors selected by the user are invalid, the system simply tells the user rather than crash because someone forgot the sixth digit in the hex color code. If all the inputs are valid, and the user clicks the “Generate” button, the tree will generate and be displayed in a separate window. If the tree has been generated, the user can “Save” the image using the directory dialog box that pops up.

When working on making saving images possible and generating multiple trees in one session, I had to work out a lot of bugs. First, I had to know if the user had closed the window to see if Turtle needed to be restarted, which took a long while to figure out. Now, whether the user keeps the second window open or not, the tree should generate just fine, but closing the window after generating works best now.

Further Development:

There are a few bugs that I haven’t worked out quite yet. The first is that when the program tells the user they’re using “Invalid Colors,” the GUI blinks rather than change seamlessly. This could likely be fixed by adjusting the window size, though it doesn’t present a major problem. Additionally, the directory dialog box doesn’t like to close on its own, though I’m not sure how to address this.

There are additional features I hope to add to the program, if I get the chance. One of them is a way to preview selected inputs. The color input would update automatically, changing the color of the text entry box based on the color input. The other inputs would be previewed in a side window, showing only one layer of the tree, so users could adjust the angle and offset with real-time feedback.
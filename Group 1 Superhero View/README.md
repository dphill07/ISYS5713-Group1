# Group 1 Superhero API Viewer<!-- omit from toc -->


</br>

# Step 1: Cloning the required repositories
To get started, you will need to clone Group 3's repository located at https://github.com/lacey92987/ISYS-5713-Group-3-Project- to your local machine.
After cloning Group 3's repository, do the same for Group 1's repository located at https://github.com/dphill07/ISYS5713-Group1.

</br>

# Step 2: Installing dependencies
First, you will need to install the dependencies for the API. To do this, open GIT CMD and navigate to the location where you cloned Group 3's repository on your local machine. Once GIT CMD is in the correct directory, run the following command:

```bash
pip install -r requirements.txt
```
---

After installing the dependencies for the API, you will need to install a few additional dependencies for the Superhero API Viewer. To do this, open GIT CMD and navigate to the directory where you cloned Group 1's repository, then navigate to the 'Group 1 Superhero View' folder. Once GIT CMD is in the correct directory, run the same command as before:

```bash
pip install -r requirements.txt
```

</br>

# Step 3: Running the API and Viewer
To run the API, in GIT CMD, navigate to the location where you cloned Group 3's repository on your local machine and run the following command:

```bash
python api.py
```

This will start the API so that you can successfully make calls to it on your local machine.

To run the viewer, open another instance of GIT CMD and navigate to the directory where the 'Group 1 Superhero View' folder is located and run the following command:

```bash
python superheroes.py
```

</br>

# Using the Superhero API Viewer
Once the viewer is running, you should see the Main Menu as shown below:

**TODO:** Add image of main menu

![test1](https://github.com/dphill07/ISYS5713-Group1/blob/main/Group%201%20Superhero%20View/README%20Images/Main%20Screen.png)

You have four options: 1. Show Heroes, 2. Thanos Snap, 3. Bring Heroes Back, and 0. Quit.

**Option 0** simply closes the program and returns you to the prompt interface.

**Option 1** takes you to the Hero Viewer screen, where you will be prompted to enter the number of heroes you would like to view at a time. The lower the number, the faster the results will be returned. However, you can enter any whole number you would like.

**TODO:** Add image of Hero Viewer

![](https://github.com/dphill07/ISYS5713-Group1/blob/main/Group%201%20Superhero%20View/README%20Images/Main%20Screen.png)

After entering a number, it will display the heroes in alphabetical order, giving their name at the top, followed by a table that contains their main stats, then another table that displays that heroes powers. The colors of the tables are formatted based on the hero's alignment. Green = good, Red = bad, and Yellow = neutral.

After displaying the requesting number of heroes, you have the option to either continue by pressing 'enter' or if you would like to stop, type 'cancel' then press enter. Typing 'cancel' will take you back to the main menu.

**TODO:** Add image of Hero Viewer

**Option 2** takes you to the THANOS SNAP menu. It will ask if you want to snap your fingers, and you can respond with 1 for 'Yes' or 2 for 'No'. If you choose option 2, it will revert to the main menu. If you choose option 1, you will receive a warning about what you are about to do. Choosing option 2 once again reverts you to the main menu. If you choose option 1, however, you will see a gif of Thanos snapping:

**TODO:** Add image of Thanos Snap

Followed by each hero that is being removed flickering just below the gif:

**TODO:** Add image of Thanos Snap

Once that is done, it will list all the heroes that remain and return you to the main menu:

**TODO:** Add image of Thanos Snap

**Option 3** allows you to bring all the heroes back. Selecting '3' brings you to the following screen, asking if you would like to bring them back:

**TODO:** Add image of bringing heroes back

Choosing 'no' reverts you to the main menu. Choosing 'yes' brings all the heroes back, and displays a message that they have been brought back. It then sends you back to the main menu, where you can view them all once again.

**TODO:** Add image of bringing heroes back

However, if you would like to play with their lives, you can snap them out of existence and bring them back as many times as you would like.

***Happy Snapping!***
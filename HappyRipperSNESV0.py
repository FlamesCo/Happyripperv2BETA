import java.awt.*;

import javax.swing.*;

public class LevelEditor extends JFrame {

   private static final long serialVersionUID = 1L;

   
   public LevelEditor() {
       setTitle("Level Editor");
       setSize(800, 600);
       setLocationRelativeTo(null);
       setDefaultCloseOperation(EXIT_ON_CLOSE);

       JPanel panel = new JPanel();
       panel.setLayout(new BorderLayout());

       

       JTabbedPane tabbedPane = new JTabbedPane();

       

       JComponent panel1 = makeTextPanel("Level 1");
       tabbedPane.addTab("Level 1", panel1);

       

       JComponent panel2 = makeTextPanel("Level 2");
       tabbedPane.addTab("Level 2", panel2);

       

       JComponent panel3 = makeTextPanel("Level 3");
       tabbedPane.addTab("Level 3", panel3);

       

       panel.add(tabbedPane, BorderLayout.CENTER);

       

       add(panel, BorderLayout.CENTER); 		// Adds Panel to frame so that it is visible								// frame visible    }    private static void createAndShowGUI() {         //Create and set up the window.         LevelEditor frame = new LevelEditor();         //Display the window.         frame.setVisible(true);     }    public static void main(String[] args) {         //Schedule a job for the event-dispatching thread:         //creating and showing this application's GUI.         javax.swing.SwingUtilities.invokeLater(new Runnable() {             public void run() {                 createAndShowGUI();             }         });     }
}
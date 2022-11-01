/**
School: Stevens Institute of Technology
Topic: Practice of Chapter 8, 9
* * *
Implemented: 27/10/2022
Coder Name: Yujun Kong
Enrolled Class: CS-501_WS
Description: File Analyzing and Content Sorting
*/

package Project_05;

public class OutputContent {
	
	/** default constructor */
	public OutputContent() {
		
	}
	
	/** overloaded constructor with argument */
	public OutputContent(String alyzdFile) {
		
		InputFile file = new InputFile(alyzdFile);
		Analysis.sortWdsList(Analysis.setNumList(file.getWords()));
		Analysis.toWdsList();
		Analysis.fnlzdList();
	}
	
	// print output content
	public void printOutput() {
		
		for (int i = 0; i < Analysis.getFlzdList().size(); i++) {
			System.out.println(Analysis.getFlzdList().get(i));
		}
	}
	
	/** program entrance */
	public static void main(String[] args) {
		
		OutputContent output = new OutputContent("inPoem.txt");
		
		System.out.println("Poem Word Analysis\n" + "\n   " + "Opening input file....\n");
		System.out.println("   Word   Frequency   Palindrome\n  -------------------------------\n");		
		output.printOutput();		
		System.out.println("\n   " + "End of results.");
		
		System.exit(0);
	}

} /** end of programming */

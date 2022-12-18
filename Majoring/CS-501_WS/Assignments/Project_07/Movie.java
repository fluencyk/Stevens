/**
 * School: Stevens Institute of Technology
 * Topic: Practice of Chapter 8, 9
 * * *
 * Implemented: 11/30/2022
 * Coder Name: Yujun Kong
 * Enrolled Class: CS-501_WS
 * Description: Inheritance Techniques
 */

package Project_07;

import java.util.ArrayList;

public class Movie extends DtrAndCpr {
	
	private String movieTitle;
	private String yearReleased;
	private String genre;
	private String rating;
	private String[] movieInfo;
	
	/** default constructor, currently using */
	public Movie() {
		
	}
	
	/** manual testing for checking any list */
	@SuppressWarnings("unused")
	private static void manualTestPrint(Object obj) {
		
		int size = 0;
		if (obj instanceof ArrayList) {
			size = ((ArrayList<?>) obj).size();
		}
		for (int i = 0; i < size; i++) {
			System.out.println(((ArrayList<?>) obj).get(i));
		}
	}
	
	// getter of each movie instance's title
	public String getMovieTitle() {
		
		return movieTitle;
	}
	
	// getter of each movie instance's released year
	public String getYearReleased() {
		
		return yearReleased;
	}
	
	// getter of each movie instance's genre
	public String getGenre() {
		
		return genre;
	}
	
	// getter of each movie instance's rating
	public String getRating() {
		
		return rating;
	}
	
	// setter of each movie instance's all core data fields
	public void setMovieInfo(String strLine) {
		
		movieInfo = strLine.split(", ");
		movieTitle = movieInfo[0];
		yearReleased = movieInfo[1];
		genre = movieInfo[2];
		rating = movieInfo[3];
		
	}
	
	/** program entrance, <- manual testing case, DO NOT regard this as main program entrance! */
	// uncomment below for testing manually
	public static void main(String[] args) {
		
		/* Movie movie = new Movie();
		movie.setInFilePath("MovieListing.txt");
		movie.prcsInFileToStdbyLines();
		manualTestPrint(movie.stdbyLines); */
	}

}

package Project_08;

import java.io.*;
import java.util.*;

public class Planet {
	
	protected String inFilePath;
	
	protected static final double PI = 3.14159;
	protected static final double weightOnEarth = 5.97237 * Math.pow(10, 24);
	protected String name;
	protected double radius;
	protected double weightRatio;
	protected double distanceFromSun;
	
	protected double surfaceArea;
	protected double circumference;
	protected double weight;
	
	private ArrayList<String[]> allPlanetsInfo = new ArrayList<String[]>();

	/** default constructor */
	public Planet() {}
	
	/** overloaded constructor */
	public Planet(String planetInfoFileName) {
		
		this.inFilePath = "src/Project_08/" + planetInfoFileName;
		try {
			this.getAllPlanetsInfo();
		} catch (FileNotFoundException e) {
			System.out.println("No such file - '" + planetInfoFileName 
			+ "'! Program ends after clicked OK button.");
		}
	}
	
	//
	protected ArrayList<String[]> getAllPlanetsInfo() throws FileNotFoundException {		
		
		File inFile = new File(inFilePath);
		try (Scanner in = new Scanner(inFile)) {
			while(in.hasNext()) {
				String[] line = in.nextLine().split(", ");
				allPlanetsInfo.add(line);
			}
		}
		return allPlanetsInfo;
	}
	
	//
	protected void setCurrPlanetInfo(String planetName) {
		
		this.name = planetName;
		for (int i = 0; i < allPlanetsInfo.size(); i++) {
			if (allPlanetsInfo.get(i)[0].equals(planetName)) {
				this.radius = Double.parseDouble(allPlanetsInfo.get(i)[1]);
				this.weightRatio = Double.parseDouble(allPlanetsInfo.get(i)[2]);
				this.distanceFromSun = Double.parseDouble(allPlanetsInfo.get(i)[3]);
				this.surfaceArea = 4 * PI * Math.pow(this.radius, 2);
				this.circumference = 2 * PI * this.radius;
				this.weight = weightOnEarth * this.weightRatio;
			}
		}
	}
	
	//
	public static void main(String[] args) {

		Planet cp = new Planet("PlanetInfos.txt");
		cp.setCurrPlanetInfo("Jupiter");
		System.out.println(cp.distanceFromSun);
	}

}

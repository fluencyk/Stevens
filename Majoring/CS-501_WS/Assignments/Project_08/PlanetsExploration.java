package Project_08;

public class PlanetsExploration extends Planet {
	
	/** default constructor */
	public PlanetsExploration() {}
	
	/** overloaded constructor */
	public PlanetsExploration(String planetInfoFileName) {
		super(planetInfoFileName);
	}
	
	//
	public void showDashboard() {
		
		
	}

	public static void main(String[] args) {
	
		PlanetsExploration pe = new PlanetsExploration("PlanetInfo.txt");
		pe.setCurrPlanetInfo("Jupiter");
		System.out.println(pe.distanceFromSun);
	}

}

/**
 * School: Stevens Institute of Technology
 * Topic: Practice of Chapter 10, 11, 12
 * * *
 * Implemented: 12/12/2022
 * Coder Name: Yujun Kong
 * Enrolled Class: CS-501_WS
 * Description: JavaFX Programming
 */

package application;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

import javafx.application.Application;
import javafx.scene.*;
import javafx.scene.control.*;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.*;
import javafx.event.*;
import javafx.geometry.Insets;
import javafx.geometry.Pos;

public class PlanetsExploration extends Application {
	
	/** fields of radio boxes */
	public RadioButton mercuryRB;
	public RadioButton venusRB;
	public RadioButton earthRB;
	public RadioButton marsRB;
	public RadioButton jupiterRB;
	public RadioButton saturnRB;
	public RadioButton uranusRB;
	public RadioButton neptuneRB;
	
	/** fields of check boxes */
	public CheckBox surfaceAreaCB;
	public CheckBox circumferenceCB;
	public CheckBox distanceCB;
	public CheckBox weightCB;
	
	/** fields of currently storing, calculating, and resulting needed data */
	public String currPlanetName;
	public String currRltHeader;	
	public Label rltHeader;
	public Label rltSurfaceArea;
	public Label rltCircumference;
	public Label rltDistance;
	public Label rltWeight;
	
	/** default constructor */
	public PlanetsExploration() {}
	
	/** renders java_fx window */
	@Override
	public void start(Stage primaryStage) {

		Label welcomeHeader = new Label("Welcome to Planets Exploration!");
		
		mercuryRB = new RadioButton("Mercury");
		venusRB = new RadioButton("Venus");
		earthRB = new RadioButton("Earth");
		marsRB = new RadioButton("Mars");
		jupiterRB = new RadioButton("Jupiter");
		saturnRB = new RadioButton("Saturn");
		uranusRB = new RadioButton("Uranus");
		neptuneRB = new RadioButton("Neptune");
		
		mercuryRB.setSelected(true);
		
		ToggleGroup radioGroup = new ToggleGroup();
		mercuryRB.setToggleGroup(radioGroup);
		venusRB.setToggleGroup(radioGroup);
		earthRB.setToggleGroup(radioGroup);
		marsRB.setToggleGroup(radioGroup);
		jupiterRB.setToggleGroup(radioGroup);
		saturnRB.setToggleGroup(radioGroup);
		uranusRB.setToggleGroup(radioGroup);
		neptuneRB.setToggleGroup(radioGroup);
		
		surfaceAreaCB = new CheckBox("Surface Area");
		circumferenceCB = new CheckBox("Circumference");
		distanceCB =  new CheckBox("Distance from Sun");
		weightCB = new CheckBox("Planet Weight");
		
		Button explore = new Button("Explore the Details");
		explore.setOnAction(new Planet("PlanetInfo.txt"));
		
		rltSurfaceArea = new Label();
		rltCircumference = new Label();
		rltDistance = new Label();
		rltWeight = new Label();
		
		HBox winHeaderHB = new HBox(20, welcomeHeader);
		winHeaderHB.setPrefHeight(10);
		winHeaderHB.setAlignment(Pos.TOP_CENTER);
		
		Label radioHeader = new Label("Select a Planet:");
		HBox radioHeaderHB = new HBox(radioHeader);
		radioHeaderHB.setMinHeight(10);
		HBox firstLineRadioHB = new HBox(20, mercuryRB, venusRB, earthRB, marsRB, jupiterRB);
		firstLineRadioHB.setAlignment(Pos.TOP_CENTER);		
		HBox secondLineRadioHB = new HBox(20, saturnRB, uranusRB, neptuneRB);
		secondLineRadioHB.setAlignment(Pos.TOP_CENTER);
		
		VBox allRadiosVB = new VBox(20, radioHeaderHB, firstLineRadioHB, secondLineRadioHB);
		allRadiosVB.setMaxHeight(60);
		allRadiosVB.setStyle("-fx-padding: 10;" + "-fx-border-style: solid inside;"
				+ "-fx-border-width: 1;" + "-fx-border-insets: 3;"
				+ "-fx-border-radius: 3;" + "-fx-border-color: lightgrey;");
		
		Label checkBoxHeader = new Label("Select One or Multiple Details:");
		HBox checkBoxHeaderHB = new HBox(checkBoxHeader);
		HBox checkBoxHB = new HBox(20, surfaceAreaCB, circumferenceCB, distanceCB, weightCB);
		checkBoxHB.setAlignment(Pos.CENTER);
		
		VBox checkBoxWithHeaderVB = new VBox(20, checkBoxHeaderHB, checkBoxHB);
		checkBoxWithHeaderVB.setStyle("-fx-padding: 10;" + "-fx-border-style: solid inside;"
				+ "-fx-border-width: 1;" + "-fx-border-insets: 3;"
				+ "-fx-border-radius: 3;" + "-fx-border-color: lightgrey;");
		
		
		HBox buttonHB = new HBox(20, explore);
		buttonHB.setAlignment(Pos.CENTER);
		buttonHB.setPrefHeight(40);
		
		currPlanetName = "";
		currRltHeader = "";
		rltHeader = new Label(currPlanetName + currRltHeader);
		HBox rltHeaderHB = new HBox(10, rltHeader);
		rltHeaderHB.setAlignment(Pos.CENTER);
		rltSurfaceArea = new Label();
		rltCircumference = new Label();
		rltDistance = new Label();
		rltWeight = new Label();
		VBox rltDetails = new VBox(20, rltSurfaceArea, rltCircumference, rltDistance, rltWeight);
		rltDetails.setAlignment(Pos.CENTER);
		VBox resultVB = new VBox(30, rltHeaderHB, rltDetails);
		resultVB.setAlignment(Pos.CENTER);
		resultVB.setStyle("-fx-padding: 10;" + "-fx-border-style: solid inside;"
				+ "-fx-border-width: 1;" + "-fx-border-insets: 3;"
				+ "-fx-border-radius: 3;" + "-fx-border-color: lightgrey;");
		
		VBox mainVBox = new VBox(10, winHeaderHB, allRadiosVB, checkBoxWithHeaderVB, buttonHB, resultVB);		
		mainVBox.setAlignment(Pos.CENTER);
		mainVBox.setPadding(new Insets(20));
		
		Scene scene = new Scene(mainVBox);
		primaryStage.setScene(scene);
		primaryStage.setTitle("Planet Exploration in Solar System");
		primaryStage.resizableProperty().setValue(Boolean.FALSE);
		primaryStage.setAlwaysOnTop(true);
		primaryStage.show();
	}
	
	// nested handler class of event processing
	public class Planet implements EventHandler<ActionEvent> {
		
		/** field of path of file of planets data */
		protected String inFilePath;
		
		/** fields of constant */
		private static final double PI = 3.14159;
		private static final double weightOnEarth = 5.972 * Math.pow(10, 24);
		
		/** fields of attributes of a planet, preset and calculated */
		private String name;
		private double radius;
		private double weightRatio;
		
		private double distanceFromSun;
		
		private double surfaceArea;
		private double circumference;
		private double weight;
		
		/** field of holding data of current planet */
		private ArrayList<String[]> allPlanetsInfo = new ArrayList<String[]>();

		/** default constructor */
		public Planet() {}
		
		/** overloaded constructor */
		public Planet(String planetInfoFileName) {
			
			this.inFilePath = "src/application/" + planetInfoFileName;
			try {
				this.getAllPlanetsInfo();
			} catch (FileNotFoundException e) {
				System.out.println("No such file - '" + planetInfoFileName 
				+ "'! Program ends after clicked OK button.");
			}
		}
		
		// fetches data from file of planets info and then holds
		private ArrayList<String[]> getAllPlanetsInfo() throws FileNotFoundException {		
			
			File inFile = new File(inFilePath);
			try (Scanner in = new Scanner(inFile)) {
				while(in.hasNext()) {
					String[] line = in.nextLine().split(", ");
					allPlanetsInfo.add(line);
				}
			}
			return allPlanetsInfo;
		}
		
		// setter of current planet info details
		private void setCurrPlanetInfo(String planetName) {
			
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
		
		// re_setter of calculated fields
		private void msgReset() {
			
			rltSurfaceArea.setText("");
			rltCircumference.setText("");
			rltDistance.setText("");
			rltWeight.setText("");
		}
		
		// handler of event actions
		@Override
		public void handle(ActionEvent event) {
			
			if (mercuryRB.isSelected()) {
				this.setCurrPlanetInfo("Mercury");
			} else if (venusRB.isSelected()) {
				this.setCurrPlanetInfo("Venus");
			} else if (earthRB.isSelected()) {
				this.setCurrPlanetInfo("Earth");
			} else if (marsRB.isSelected()) {
				this.setCurrPlanetInfo("Mars");
			} else if (jupiterRB.isSelected()) {
				this.setCurrPlanetInfo("Jupiter");
			} else if (saturnRB.isSelected()) {
				this.setCurrPlanetInfo("Saturn");
			} else if (uranusRB.isSelected()) {
				this.setCurrPlanetInfo("Uranus");
			} else if (neptuneRB.isSelected()) {
				this.setCurrPlanetInfo("Neptune");
			}
			
			if (surfaceAreaCB.isSelected() || circumferenceCB.isSelected() || 
			distanceCB.isSelected() || weightCB.isSelected()) {
				currPlanetName = name;
				currRltHeader = "'s Details Explored";
				rltHeader.setText(currPlanetName + currRltHeader);
			} else { /* I don't think here needs to throws a exception though there is a guidance of
			 		  asking us to use some exception throwing. Please kindly check the requirements,
			 		  No text fields need to be implemented, if I understood correctly.*/ 
				rltHeader.setText("Please at least select one of the checkboxs of the planet's details");
				this.msgReset();
			}
			
			if (surfaceAreaCB.isSelected()) {
				rltSurfaceArea.setText("Surface Area: " + String.format("%,.3f", surfaceArea) + " KM^2");
			} else {
				rltSurfaceArea.setText("");
			}
			
			if (circumferenceCB.isSelected()) {	
				rltCircumference.setText("Circumference: " + String.format("%,.3f", circumference) + " KM");
			} else {
				rltCircumference.setText("");
			}
			
			if (distanceCB.isSelected()) {
				rltDistance.setText("Distance from Sun: " + String.format("%,.3f", distanceFromSun) + " AU");
			} else {
				rltDistance.setText("");
			}
			
			if (weightCB.isSelected()) {
				rltWeight.setText("Weight of the Planet: " + String.format("%,.3f", weight) + " KG (Roughly)");
			} else {
				rltWeight.setText("");
			}
		}
	}
	
	/** main program entrance! */
	public static void main(String[] args) {
		launch(args);
	}
	
} /** end of programming */

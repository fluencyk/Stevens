/**
School: Stevens Institute of Technology
Topic: Practice of Chapter 6, 7
* * *
Implemented: 15/09/2022
Coder Name: Yujun Kong
Enrolled Class: CS-501_WS
Description: Classes design in coupling, depending, modeling
*/

package Project_04;

public class Triangle {

	private double base;
	private double height;
	
	public Triangle() {
		
		this.base = 0.0;
		this.height = 0.0;
	}
	
	public Triangle(double baseVal, double heigVal) {
		
		this.setRadiusVal(baseVal, heigVal);
	}
	
	public void setRadiusVal(double bsVal, double hgVal) {
		
		this.base = bsVal;
		this.height = hgVal;
	}
	
	public double getBase() {
		
		return this.base;
	}
	
	public double getHeight() {
		
		return this.height;
	}
	
	public double computeArea() {
		
		return (this.getBase() * this.getHeight()) / 2;
	}

}
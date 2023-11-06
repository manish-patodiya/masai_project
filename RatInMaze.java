import java.util.Random;
import java.util.Scanner;

public class RatInMaze {
	
	char wall = '|',open='-',path='*';
	int n;
	char maze[][];
	int visited[][];
	
	public boolean find_path(int i,int j) {
		if(i<0 || i>n-1 || j<0 || j>n-1 || maze[i][j] == wall || visited[i][j] == 1) return false;
		if(i==n-1 && j==n-1) return true;
		
		
		visited[i][j] = 1;
		if(find_path(i+1,j)  || find_path(i,j+1) || find_path(i-1,j) || find_path(i,j-1)){
			maze[i][j] = path;
			return true;
		}
		return false;
	}
	
	public void generate_maze() {
		Random random = new Random();
		maze = new char[n][n];
		visited = new int[n][n];
		
		// assign open space for all the cells
		for(int i=0;i<n;i++) 
			for(int j=0;j<n;j++) 
				maze[i][j] = open;
		
		// construct walls with restriction of 25%
		for(int i=0;i<n;i++) {
			int max = (int)(0.25 * n);
			for(int j=0;j<max;j++) 
					maze[i][random.nextInt(n)] = wall;
			
		}
		
		// define start and end position
		maze[0][0] = 'S';
		maze[n-1][n-1] = 'E';
				
		// print generated maze
		System.out.println("Generated Maze: ");
		print_maze();
	}
	
	public void print_maze() {
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++)	
				System.out.print(maze[i][j]+" ");
			System.out.println();
		}
	}
	
	public static void options() {
		System.out.println();
		System.out.println("1. Print the path");
		System.out.println("2. Generate another puzzle");
		System.out.println("3. Exit the Game");
		System.out.print("Enter your choice (1/2/3): ");
	}

	@SuppressWarnings("resource")
	public static void main(String[] args) {
		
		Maze m = new Maze();
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter the size of the maze: ");
		m.n = sc.nextInt();		
		m.generate_maze();
		
		while(true){
			options();
			int inp = sc.nextInt();
			switch (inp) {
			case 1:
				if(m.find_path(0, 0)) {					
					System.out.println("Maze with Path:");
					m.print_maze();
				}else {
					System.out.println("No Path found!");
				}
				return;
			case 2:
				m.generate_maze();
				break;
			default:
				return;
			}
		}
	}

}

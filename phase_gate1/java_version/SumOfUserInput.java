import java.util.Scanner;
public class SumOfUserInput{
	public static void main(String... arg){
		Scanner sc = new Scanner(System.in);

int sumOfUserinput = 0;
System.out.print("Enter number between 0 and 1000: ");
int numbers = sc.nextInt(); 

while (numbers > 0) {
	sumOfUserinput += numbers % 10;
	numbers = numbers / 10;
	}       

System.out.print("The sum of the numbers imputed is :" + sumOfUserinput);

	}
}
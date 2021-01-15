import java.util.Scanner;

public class convertisseur {
	public static void main (String[] args) {

		char loop = ' ';
		
		Scanner sc = new Scanner(System.in);
		
		do {

			System.out.println("-------------------------------------------------");
			System.out.println("CONVERTISSEUR DEGRES CELSIUS ET DEGRES FAHRANHEIT");
			System.out.println("-------------------------------------------------");
			
			char choice = ' ';
			float degre = 0.0f;
			
			do {
				
				System.out.println("Choisissez le mode de convertion :");
				System.out.println("1 - Convertisseur Celsius / Fahranheit");
				System.out.println("2 - Convertisseur Fahranheit / Celsius");
				choice = sc.nextLine().charAt(0);
				
				if (choice != '1' && choice != '2') {
					System.out.println("Mauvais choix !");
				}
				
			}while (choice != '1' && choice != '2');
			
			System.out.println("Température a convertir : ");
			degre = sc.nextFloat();
			sc.nextLine();
			
			float result = 0.0f;
			
			if (choice == '1') {
				result = ( (float) (9) / (float) (5) * degre) + 32;
				System.out.println(degre + " °C correspond à : " + result + " °F.");
			}
			else if (choice == '2') {
				result = ((degre - (float) (32) ) * (float) (5) ) / (float) (9);
				System.out.println(degre + " °F correspond à : " + result + " °C.");
			}
			
			do {
				
				System.out.println("Retry ? (O/N)");
				loop = sc.nextLine().charAt(0);
				
			}while (loop != 'O' && loop != 'N');
			
		}while (loop == 'O');
		
		System.out.print("Au revoir !\n");
	}
}
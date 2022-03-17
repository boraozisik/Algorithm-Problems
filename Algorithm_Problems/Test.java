
public class Test {
    public static void main(String[] args) {
        User u1 = new User("Bora09", " Abdullah Bora", "Özışık", "07.11.2000", "1234", "abdullahbora@cbu.com", "aydın", "aydın");
        u1.loginToSystem("Bora09", "1234");
	u1.viewUserInformation();
	System.out.println("*****************************************");
	CreditCard c1 = new CreditCard("223524534", u1, "3409", "2028");
	c1.viewCreditCardInformation();
	System.out.println("*****************************************");
	Product p1 = new Product("Suç ve Ceza", "Yellow", "Book", 50, 100, "Suç ve Ceza is a book and author ==> Fyodor Dostoyevski");
	Product p2 = new Product("rtx Watch", "Black", "electronic stuff ==> watch", 200, 150, "rtx is a watch");
	Product p3 = new Product("Shirt", "Green", "Clothes", 400, 80, "Green summer Shirt");
	p1.viewProductInformation();
	System.out.println("------------------------------------------");
	p2.viewProductInformation();
	System.out.println("------------------------------------------");
	p3.viewProductInformation();
	System.out.println("------------------------------------------");
	System.out.println("*****************************************");
	u1.addToFavoriteProducts(p1);
	u1.addToFavoriteProducts(p2);
	System.out.println("------------------------------------------");
	u1.viewFavoriteProducts();
	System.out.println("*****************************************");
	Order o1 = new Order(u1, p3, c1);
        u1.orderProduct(250,o1);
        System.out.println("*****************************************");
	u1.viewOrderedProducts();
        System.out.println("*****************************************");
        u1.orderProduct(550, o1);
    }
}

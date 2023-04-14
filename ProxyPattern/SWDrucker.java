package ProxyPattern;

public class SWDrucker extends Drucker {

    @Override
    public void drucken(String text){
        System.out.println("Monochrome printing...");
        System.out.println(text + "\n");
    }
    
}

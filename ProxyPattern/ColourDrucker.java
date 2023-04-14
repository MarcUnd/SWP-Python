package ProxyPattern;

public class ColourDrucker extends Drucker {
    

    @Override
    public void drucken(String text){
        System.out.println("Colourful printing...");
        System.out.println(text + "\n");
    }
}

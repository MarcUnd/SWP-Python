package ObserverPattern;

public class Screen extends Subscriber{

    @Override
    public void getData(Data data){
        System.out.println("Screen displays: " + data.getTemp() + " °C\n");
    }

    public void getDataFromSensor(Sensor sens){
        System.out.println("Screen pulls data...");
        System.out.println("Screen displays: " + sens.getCurrentData().getTemp() + " °C\n");
    }
    
}

package ObserverPattern;

public class BigScreen extends Subscriber{

    public void getData(Data data){
        System.out.println("Big Screen displays: " + data.getTemp() + " °C\n");
    }

    public void getDataFromSensor(Sensor sens){
        System.out.println("Big Screen pulls data...");
        System.out.println("Big Screen displays: " + sens.getCurrentData().getTemp() + " °C\n");
    }
}
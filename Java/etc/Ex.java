package Java.etc;

public class Ex {
    public static void main(String[] args) {
        WelcomeBean w = welcome();
    }

    public static WelcomeBean welcome() {
        WelcomeBean wb = new WelcomeBean();
        return wb;
    }
}

class WelcomeBean {
    private String message;
    private final WelcomeBean wb = new WelcomeBean("hi");

    public WelcomeBean(String message) {
        this.message = message;
    }

    private WelcomeBean() {
    }

    public WelcomeBean getInstance() {
        return wb;
    }

    public String getMessage() {
        return message;
    }

}

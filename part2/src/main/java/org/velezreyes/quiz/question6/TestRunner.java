import org.junit.jupiter.api.JUnitCore;
import org.junit.jupiter.api.Result;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TextUI;
import org.junit.platform.engine.discovery.DiscoverySelectors;
import org.junit.platform.launcher.Launcher;
import org.junit.platform.launcher.LauncherDiscoveryRequest;
import org.junit.platform.launcher.core.LauncherFactory;

public class TestRunner {
    public static void main(String[] args) {
        // Ejecutar las pruebas
        LauncherDiscoveryRequest request = LauncherDiscoveryRequest
                .builder()
                .selectors(DiscoverySelectors.selectClass(Question6Test.class))
                .build();

        Launcher launcher = LauncherFactory.create();
        launcher.registerTestExecutionListeners(new TextUI());
        launcher.execute(request);
    }
}


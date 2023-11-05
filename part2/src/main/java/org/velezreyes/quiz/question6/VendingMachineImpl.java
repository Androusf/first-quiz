package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {
    private Map<String, Drink> availableDrinks = new HashMap<>();
    private int currentMoney = 0;

    public static VendingMachine getInstance() {
        return new VendingMachineImpl();
    }

    @Override
    public void insertQuarter() {
        currentMoney += 25; // Cada cuarto (quarter) es igual a 25 centavos.
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        if (availableDrinks.containsKey(name)) {
            Drink selectedDrink = availableDrinks.get(name);
            int drinkCost = selectedDrink.getCost();

            if (currentMoney >= drinkCost) {
                currentMoney -= drinkCost;
                return selectedDrink;
            } else {
                throw new NotEnoughMoneyException();
            }
        } else {
            throw new UnknownDrinkException();
        }
    }
}


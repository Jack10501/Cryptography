/*
 * Created by Jack Paull on 27/03/19.
*/

#include "gcdeuc.h"

/*Checks if both keys provided are valid
  Otherwise returns an error*/
int validKeys(int keyA, int keyB, int alpha){

    int greatestComDiv;

    if(keyA < 0 || keyA > 25) {
        printf("KeyA out of range 0 - 25\n");
        //Cannot be ERROR = 1 constant because gcd must return 1 to be valid
        return 2;
    }

    if(keyB < 0 || keyB > 25) {
        printf("KeyB out of range 0 - 25\n");
        //Cannot be ERROR = 1 constant because gcd must return 1 to be valid
        return 2;
    }

    greatestComDiv = gcd(keyA, alpha);
    if(greatestComDiv != 1) {
        printf("Keys are not co-prime\n");
        return 2;
    }

    // A valid key get returned
    return greatestComDiv;
}

/* Checks to see if keys are co primes of each other,
 * if 1 is returned then the keys are co primes, otherwise the keys are
 * invalid */
int gcd(int a, int b) {
    //Check if b MOD a is equal to 0, if so
    //The previous two numbers are equal and the GCD has been found
    if (a == 0) {
        return b;
    }
    //If not, mod b by a and check if that is equal on the next run
    //Works on the same principle as taking away since: 60 % 36 = 24 & 60-36 = 24
    return gcd(b % a, a);
}


/* Extended Euclidean Algorithm to find the inverse of A
 * for decryption */
int extendedGcd(int a, int n){

    int t = 0;
    // Leave n as it is needed if t becomes a negative at the end
    int r = n;
    int q = 0;
    // Temp value
    int temp = 0;
    // Variables to hold the value between loops
    int nextT = 1;
    int nextR = a;

    // Check if the key is not co prime
    if (gcd(a, n) != 1) {
        return -1;
    }

    // The loop to find the inverse
    while (nextR != 0)
    {
        // Get the quotient each time
        // First time is alphabet / key
        q = r / nextR;
        temp = t; //0
        t = nextT; //1
        nextT = temp - (q * nextT);
        // Now repeat for r
        temp = r;
        r = nextR;
        nextR = temp - (q * nextR);
    }

    // Ensure the value doesnt end up as a negative
    if (t < 0) {
        t = t + n;
    }

    // Return the found inverse
    return t;
}
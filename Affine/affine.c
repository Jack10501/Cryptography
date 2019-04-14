/*
 * Created by Jack Paull on 25/03/19
 * Takes an input file and either encrypts or decrypts its
 * contents using Affine Cypher
 * Uses the English alphabet and ignores non-letter symbols
*/

#include "affine.h"


int main(int argc, char *argv[]) {

    // Check number of args are correct
    if(argc != ARGS) {
        fprintf(stderr, "Requires <Flag> <Input File> <Output File> <Key A> <Key B>\n"
                        "Process Exited\n");
        return ERROR;
    }

    int keyA = atoi(argv[4]);
    int keyB = atoi(argv[5]);
    char *flag = argv[1], nextChar;
    FILE *fIn = fopen(argv[2], "r");
    FILE *fOut = fopen(argv[3], "w");

    // Check File
    if(fIn == NULL || fOut == NULL) {
        fprintf(stderr, "File Paths Incorrect\n"
                        "Process Exited\n");
        return ERROR;
    }

    // Check Keys
    if(validKeys(keyA, keyB, ALPHA) != 1) {
        fprintf(stderr, "Keys incorrect\n"
                        "Process Exited\n");
        return ERROR;
    }


    //FunctionPointer created for encryption or decryption
    FuncPtr fp;

    // Check Flags
    if(!strncmp(flag, "-e", 2)) {
        fp = &encrypt;
    } else if(!strncmp(flag, "-d", 2)) {
        fp = &decrypt;
    } else {
        fprintf(stderr, "Flag incorrect, use either \"-e\" to encrypt"
                        "or \"-d\" to decrypt\n"
                        "Process Exited\n");
        return ERROR;
    }

    while(feof(fIn) == 0 && ferror(fIn) == 0 && ferror(fOut) == 0) {
        //This will also grab an EOF char but this is negated in the next if statement
        nextChar = fgetc(fIn);
        //TEST
        printf(" %c =>", nextChar);

        //Ensures an end of file char isn't placed into the output file
        if(feof(fIn) == 0) {
            //Put new char into the output file
            fputc((*fp)(nextChar, keyA, keyB), fOut);
        }

        //TEST
        printf("\n");
    }

    //Close the input and output files
    fclose(fIn);
    fclose(fOut);

    return 0;
}

/*Encrypts the given char using Affine Cipher
  Ignores non-letter characters*/
char encrypt(char txt, int keyA, int keyB) {
    // CipherText = PlainText * a + b
    // Must add take A/a so that the ascii e.g. a's ascii becomes 0
    // and matches our table that runs from 0-25, then add the a back on
    // so the ascii is back in the a-z/A-Z range

    // Only checks for upper or lower case letters using isupper/lower from ctype.h
    if (isupper(txt)) {
        //TEST
        printf(" %c", ((((int)txt - 'A') * keyA + keyB) % ALPHA) + 'A');
        return ((((int)txt - 'A') * keyA + keyB) % ALPHA) + 'A';
    } else if (islower(txt)) {
        //TEST
        printf(" %c", ((((int)txt - 'a') * keyA + keyB) % ALPHA) + 'a');
        return ((((int)txt - 'a') * keyA + keyB) % ALPHA) + 'a';
    }

    // Ignores non-letter characters and returns plain text
    return txt;
}

//Decrypts the given char using Affine Cipher
char decrypt(char txt, int keyA, int keyB) {
    int inverse = extendedGcd(keyA, ALPHA);

    if(isupper(txt)) {
        return ((inverse * (txt - 'A' - keyB + ALPHA)) % ALPHA) + 'A';
    } else if(islower(txt)) {
        return ((inverse * (txt - 'a' - keyB + ALPHA)) % ALPHA) + 'a';
    }

    //Otherwise return the space or original non-letter plaintext
    return txt;
}

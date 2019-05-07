/*
 * Created by Jack Paull on 25/03/19
 * Header file for affine.c
*/

#ifndef AFFINE_H
#define AFFINE_H

#ifndef STANDARD
#define STANDARD
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#endif //STANDARD

#include "gcdeuc.h"

char encrypt(char,int,int);
char decrypt(char,int,int);

typedef char (*FuncPtr)(char,int,int);

//Define constants
#define ARGS 6
#define ALPHA 26
#define ERROR 1

#endif //AFFINE_H

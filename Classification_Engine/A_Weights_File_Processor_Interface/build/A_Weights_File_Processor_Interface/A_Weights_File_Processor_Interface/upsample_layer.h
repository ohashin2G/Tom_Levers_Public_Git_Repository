#ifndef UPSAMPLE_LAYER_H
#define UPSAMPLE_LAYER_H


#include "darknet.h"


layer make_upsample_layer(int batch, int w, int h, int c, int stride);
void forward_upsample_layer(const layer l, network_state state);
void backward_upsample_layer(const layer l, network_state state);


#endif
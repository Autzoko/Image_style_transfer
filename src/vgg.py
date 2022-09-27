# Trying to implement VGG19 network by using pytorch
import os

import torch
import torch.nn as nn


class Conv(nn.Module):
	def __init__(self, input_channels, output_channels, kernel_size=1, stride=1, padding=None, groups=1, activation=True):
		super(Conv, self).__init__()

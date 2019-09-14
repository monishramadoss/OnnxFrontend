from . import *
layer={}

from . import LSTM
layer['LSTM'] = {1: LSTM.LSTM_1, 7: LSTM.LSTM_7}
from . import Identity
layer['Identity'] = {1: Identity.Identity_1}
from . import Abs
layer['Abs'] = {1: Abs.Abs_1, 6: Abs.Abs_6}
from . import BatchNormalization
layer['BatchNormalization'] = {1: BatchNormalization.BatchNormalization_1, 6: BatchNormalization.BatchNormalization_6, 7: BatchNormalization.BatchNormalization_7, 9: BatchNormalization.BatchNormalization_9}
from . import Mean
layer['Mean'] = {1: Mean.Mean_1, 6: Mean.Mean_6, 8: Mean.Mean_8}
from . import Add
layer['Add'] = {1: Add.Add_1, 6: Add.Add_6, 7: Add.Add_7}
from . import GlobalMaxPool
layer['GlobalMaxPool'] = {1: GlobalMaxPool.GlobalMaxPool_1}
from . import Cast
layer['Cast'] = {1: Cast.Cast_1, 6: Cast.Cast_6, 9: Cast.Cast_9}
from . import AveragePool
layer['AveragePool'] = {1: AveragePool.AveragePool_1, 7: AveragePool.AveragePool_7, 10: AveragePool.AveragePool_10}
from . import And
layer['And'] = {1: And.And_1, 7: And.And_7}
from . import LRN
layer['LRN'] = {1: LRN.LRN_1}
from . import ArgMax
layer['ArgMax'] = {1: ArgMax.ArgMax_1}
from . import Resize
layer['Resize'] = {10: Resize.Resize_10}
from . import Expand
layer['Expand'] = {8: Expand.Expand_8}
from . import Neg
layer['Neg'] = {1: Neg.Neg_1, 6: Neg.Neg_6}
from . import Mul
layer['Mul'] = {1: Mul.Mul_1, 6: Mul.Mul_6, 7: Mul.Mul_7}
from . import ArgMin
layer['ArgMin'] = {1: ArgMin.ArgMin_1}
from . import Exp
layer['Exp'] = {1: Exp.Exp_1, 6: Exp.Exp_6}
from . import Div
layer['Div'] = {1: Div.Div_1, 6: Div.Div_6, 7: Div.Div_7}
from . import ReverseSequence
layer['ReverseSequence'] = {10: ReverseSequence.ReverseSequence_10}
from . import Ceil
layer['Ceil'] = {1: Ceil.Ceil_1, 6: Ceil.Ceil_6}
from . import DepthToSpace
layer['DepthToSpace'] = {1: DepthToSpace.DepthToSpace_1}
from . import Clip
layer['Clip'] = {1: Clip.Clip_1, 6: Clip.Clip_6}
from . import RNN
layer['RNN'] = {1: RNN.RNN_1, 7: RNN.RNN_7}
from . import Concat
layer['Concat'] = {1: Concat.Concat_1, 4: Concat.Concat_4}
from . import Constant
layer['Constant'] = {1: Constant.Constant_1, 9: Constant.Constant_9}
from . import LpPool
layer['LpPool'] = {1: LpPool.LpPool_1, 2: LpPool.LpPool_2}
from . import Conv
layer['Conv'] = {1: Conv.Conv_1}
from . import Not
layer['Not'] = {1: Not.Not_1}
from . import Gather
layer['Gather'] = {1: Gather.Gather_1}
from . import ConvTranspose
layer['ConvTranspose'] = {1: ConvTranspose.ConvTranspose_1}
from . import Dropout
layer['Dropout'] = {1: Dropout.Dropout_1, 6: Dropout.Dropout_6, 7: Dropout.Dropout_7, 10: Dropout.Dropout_10}
from . import LeakyRelu
layer['LeakyRelu'] = {1: LeakyRelu.LeakyRelu_1, 6: LeakyRelu.LeakyRelu_6}
from . import Elu
layer['Elu'] = {1: Elu.Elu_1, 6: Elu.Elu_6}
from . import GlobalAveragePool
layer['GlobalAveragePool'] = {1: GlobalAveragePool.GlobalAveragePool_1}
from . import Gemm
layer['Gemm'] = {1: Gemm.Gemm_1, 6: Gemm.Gemm_6, 7: Gemm.Gemm_7, 9: Gemm.Gemm_9}
from . import MaxPool
layer['MaxPool'] = {1: MaxPool.MaxPool_1, 8: MaxPool.MaxPool_8, 10: MaxPool.MaxPool_10}
from . import Equal
layer['Equal'] = {1: Equal.Equal_1, 7: Equal.Equal_7}
from . import Tile
layer['Tile'] = {1: Tile.Tile_1, 6: Tile.Tile_6}
from . import Flatten
layer['Flatten'] = {1: Flatten.Flatten_1, 9: Flatten.Flatten_9}
from . import Floor
layer['Floor'] = {1: Floor.Floor_1, 6: Floor.Floor_6}
from . import GRU
layer['GRU'] = {1: GRU.GRU_1, 3: GRU.GRU_3, 7: GRU.GRU_7}
from . import GlobalLpPool
layer['GlobalLpPool'] = {1: GlobalLpPool.GlobalLpPool_1, 2: GlobalLpPool.GlobalLpPool_2}
from . import Greater
layer['Greater'] = {1: Greater.Greater_1, 7: Greater.Greater_7, 9: Greater.Greater_9}
from . import HardSigmoid
layer['HardSigmoid'] = {1: HardSigmoid.HardSigmoid_1, 6: HardSigmoid.HardSigmoid_6}
from . import Selu
layer['Selu'] = {1: Selu.Selu_1, 6: Selu.Selu_6}
from . import Hardmax
layer['Hardmax'] = {1: Hardmax.Hardmax_1}
from . import If
layer['If'] = {1: If.If_1}
from . import Min
layer['Min'] = {1: Min.Min_1, 6: Min.Min_6, 8: Min.Min_8}
from . import InstanceNormalization
layer['InstanceNormalization'] = {1: InstanceNormalization.InstanceNormalization_1, 6: InstanceNormalization.InstanceNormalization_6}
from . import Less
layer['Less'] = {1: Less.Less_1, 7: Less.Less_7, 9: Less.Less_9}
from . import EyeLike
layer['EyeLike'] = {9: EyeLike.EyeLike_9}
from . import RandomNormal
layer['RandomNormal'] = {1: RandomNormal.RandomNormal_1}
from . import Slice
layer['Slice'] = {1: Slice.Slice_1, 10: Slice.Slice_10}
from . import PRelu
layer['PRelu'] = {1: PRelu.PRelu_1, 6: PRelu.PRelu_6, 7: PRelu.PRelu_7, 9: PRelu.PRelu_9}
from . import Log
layer['Log'] = {1: Log.Log_1, 6: Log.Log_6}
from . import LogSoftmax
layer['LogSoftmax'] = {1: LogSoftmax.LogSoftmax_1}
from . import Loop
layer['Loop'] = {1: Loop.Loop_1}
from . import LpNormalization
layer['LpNormalization'] = {1: LpNormalization.LpNormalization_1}
from . import MatMul
layer['MatMul'] = {1: MatMul.MatMul_1, 9: MatMul.MatMul_9}
from . import ReduceL2
layer['ReduceL2'] = {1: ReduceL2.ReduceL2_1}
from . import Max
layer['Max'] = {1: Max.Max_1, 6: Max.Max_6, 8: Max.Max_8}
from . import MaxRoiPool
layer['MaxRoiPool'] = {1: MaxRoiPool.MaxRoiPool_1}
from . import Or
layer['Or'] = {1: Or.Or_1, 7: Or.Or_7}
from . import Pad
layer['Pad'] = {1: Pad.Pad_1, 2: Pad.Pad_2}
from . import RandomUniformLike
layer['RandomUniformLike'] = {1: RandomUniformLike.RandomUniformLike_1}
from . import Reciprocal
layer['Reciprocal'] = {1: Reciprocal.Reciprocal_1, 6: Reciprocal.Reciprocal_6}
from . import Pow
layer['Pow'] = {1: Pow.Pow_1, 7: Pow.Pow_7}
from . import RandomNormalLike
layer['RandomNormalLike'] = {1: RandomNormalLike.RandomNormalLike_1}
from . import OneHot
layer['OneHot'] = {9: OneHot.OneHot_9}
from . import RandomUniform
layer['RandomUniform'] = {1: RandomUniform.RandomUniform_1}
from . import ReduceL1
layer['ReduceL1'] = {1: ReduceL1.ReduceL1_1}
from . import ReduceLogSum
layer['ReduceLogSum'] = {1: ReduceLogSum.ReduceLogSum_1}
from . import ReduceLogSumExp
layer['ReduceLogSumExp'] = {1: ReduceLogSumExp.ReduceLogSumExp_1}
from . import ReduceMax
layer['ReduceMax'] = {1: ReduceMax.ReduceMax_1}
from . import IsNaN
layer['IsNaN'] = {9: IsNaN.IsNaN_9}
from . import ReduceMean
layer['ReduceMean'] = {1: ReduceMean.ReduceMean_1}
from . import ReduceMin
layer['ReduceMin'] = {1: ReduceMin.ReduceMin_1}
from . import ReduceProd
layer['ReduceProd'] = {1: ReduceProd.ReduceProd_1}
from . import ReduceSum
layer['ReduceSum'] = {1: ReduceSum.ReduceSum_1}
from . import ReduceSumSquare
layer['ReduceSumSquare'] = {1: ReduceSumSquare.ReduceSumSquare_1}
from . import Relu
layer['Relu'] = {1: Relu.Relu_1, 6: Relu.Relu_6}
from . import Reshape
layer['Reshape'] = {1: Reshape.Reshape_1, 5: Reshape.Reshape_5}
from . import Shape
layer['Shape'] = {1: Shape.Shape_1}
from . import Sigmoid
layer['Sigmoid'] = {1: Sigmoid.Sigmoid_1, 6: Sigmoid.Sigmoid_6}
from . import Size
layer['Size'] = {1: Size.Size_1}
from . import Softmax
layer['Softmax'] = {1: Softmax.Softmax_1}
from . import Softplus
layer['Softplus'] = {1: Softplus.Softplus_1}
from . import Softsign
layer['Softsign'] = {1: Softsign.Softsign_1}
from . import SpaceToDepth
layer['SpaceToDepth'] = {1: SpaceToDepth.SpaceToDepth_1}
from . import TfIdfVectorizer
layer['TfIdfVectorizer'] = {9: TfIdfVectorizer.TfIdfVectorizer_9}
from . import Split
layer['Split'] = {1: Split.Split_1, 2: Split.Split_2}
from . import Sqrt
layer['Sqrt'] = {1: Sqrt.Sqrt_1, 6: Sqrt.Sqrt_6}
from . import Squeeze
layer['Squeeze'] = {1: Squeeze.Squeeze_1}
from . import TopK
layer['TopK'] = {1: TopK.TopK_1, 10: TopK.TopK_10}
from . import Sub
layer['Sub'] = {1: Sub.Sub_1, 6: Sub.Sub_6, 7: Sub.Sub_7}
from . import Sum
layer['Sum'] = {1: Sum.Sum_1, 6: Sum.Sum_6, 8: Sum.Sum_8}
from . import Shrink
layer['Shrink'] = {9: Shrink.Shrink_9}
from . import Tanh
layer['Tanh'] = {1: Tanh.Tanh_1, 6: Tanh.Tanh_6}
from . import Transpose
layer['Transpose'] = {1: Transpose.Transpose_1}
from . import Unsqueeze
layer['Unsqueeze'] = {1: Unsqueeze.Unsqueeze_1}
from . import Xor
layer['Xor'] = {1: Xor.Xor_1, 7: Xor.Xor_7}
from . import Acos
layer['Acos'] = {7: Acos.Acos_7}
from . import Asin
layer['Asin'] = {7: Asin.Asin_7}
from . import Atan
layer['Atan'] = {7: Atan.Atan_7}
from . import Cos
layer['Cos'] = {7: Cos.Cos_7}
from . import Sin
layer['Sin'] = {7: Sin.Sin_7}
from . import Tan
layer['Tan'] = {7: Tan.Tan_7}
from . import Multinomial
layer['Multinomial'] = {7: Multinomial.Multinomial_7}
from . import Scan
layer['Scan'] = {8: Scan.Scan_8, 9: Scan.Scan_9}
from . import Compress
layer['Compress'] = {9: Compress.Compress_9}
from . import ConstantOfShape
layer['ConstantOfShape'] = {9: ConstantOfShape.ConstantOfShape_9}
from . import MaxUnpool
layer['MaxUnpool'] = {9: MaxUnpool.MaxUnpool_9}
from . import Scatter
layer['Scatter'] = {9: Scatter.Scatter_9}
from . import Sinh
layer['Sinh'] = {9: Sinh.Sinh_9}
from . import Cosh
layer['Cosh'] = {9: Cosh.Cosh_9}
from . import Asinh
layer['Asinh'] = {9: Asinh.Asinh_9}
from . import Acosh
layer['Acosh'] = {9: Acosh.Acosh_9}
from . import NonMaxSuppression
layer['NonMaxSuppression'] = {10: NonMaxSuppression.NonMaxSuppression_10}
from . import Atanh
layer['Atanh'] = {9: Atanh.Atanh_9}
from . import Sign
layer['Sign'] = {9: Sign.Sign_9}
from . import Erf
layer['Erf'] = {9: Erf.Erf_9}
from . import Where
layer['Where'] = {9: Where.Where_9}
from . import NonZero
layer['NonZero'] = {9: NonZero.NonZero_9}
from . import MeanVarianceNormalization
layer['MeanVarianceNormalization'] = {9: MeanVarianceNormalization.MeanVarianceNormalization_9}
from . import StringNormalizer
layer['StringNormalizer'] = {10: StringNormalizer.StringNormalizer_10}
from . import Mod
layer['Mod'] = {10: Mod.Mod_10}
from . import ThresholdedRelu
layer['ThresholdedRelu'] = {10: ThresholdedRelu.ThresholdedRelu_10}
from . import MatMulInteger
layer['MatMulInteger'] = {10: MatMulInteger.MatMulInteger_10}
from . import QLinearMatMul
layer['QLinearMatMul'] = {10: QLinearMatMul.QLinearMatMul_10}
from . import ConvInteger
layer['ConvInteger'] = {10: ConvInteger.ConvInteger_10}
from . import QLinearConv
layer['QLinearConv'] = {10: QLinearConv.QLinearConv_10}
from . import QuantizeLinear
layer['QuantizeLinear'] = {10: QuantizeLinear.QuantizeLinear_10}
from . import DequantizeLinear
layer['DequantizeLinear'] = {10: DequantizeLinear.DequantizeLinear_10}
from . import IsInf
layer['IsInf'] = {10: IsInf.IsInf_10}
from . import RoiAlign
layer['RoiAlign'] = {10: RoiAlign.RoiAlign_10}
from . import Upsample
layer['Upsample'] = {1: Upsample.Upsample_1}
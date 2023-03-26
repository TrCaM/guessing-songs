load("@rules_proto//proto:defs.bzl", "proto_library")
load("@protobuf//:protobuf.bzl", "py_proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "song_proto",
    srcs = ["song.proto"],
)

py_proto_library(
    name = "song_py_proto",
    srcs = ["song.proto"],
)
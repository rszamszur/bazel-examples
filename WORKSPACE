load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_cc",
    urls = ["https://github.com/bazelbuild/rules_cc/archive/8bb0eb5c5ccd96b91753bb112096bb6993d16d13.tar.gz"],
    strip_prefix = "rules_cc-8bb0eb5c5ccd96b91753bb112096bb6993d16d13",
    sha256 = "19d93d9a54487343dec4fabccf9974a9a5e8749297a448d1f310459eeca5091e",
)

http_archive(
    name = "rules_python",
    sha256 = "cdf6b84084aad8f10bf20b46b77cb48d83c319ebe6458a18e9d2cebf57807cdd",
    strip_prefix = "rules_python-0.8.1",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.8.1.tar.gz",
)

http_archive(
    name = "io_tweag_rules_nixpkgs",
    strip_prefix = "rules_nixpkgs-e554637eef44e6f3ddecb6149c13f878d0548f2a",
    urls = ["https://github.com/tweag/rules_nixpkgs/archive/e554637eef44e6f3ddecb6149c13f878d0548f2a.tar.gz"],
)

load("@io_tweag_rules_nixpkgs//nixpkgs:repositories.bzl", "rules_nixpkgs_dependencies")
rules_nixpkgs_dependencies()

load("@io_tweag_rules_nixpkgs//nixpkgs:nixpkgs.bzl", "nixpkgs_git_repository", "nixpkgs_python_configure")

nixpkgs_git_repository(
    name = "nixpkgs",
    revision = "21.11",
)

nixpkgs_python_configure(
    name = "nixpkgs_python_toolchain",
    repository = "@nixpkgs",
)

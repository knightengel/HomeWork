{ pkgs ? import <nixpkgs> {} }:

let
  my-python = pkgs.python3.withPackages (ps: with ps; [
    tkinter
  ]);
in
pkgs.mkShell {
  name = "python-search-app-env";

  buildInputs = [
    my-python
    pkgs.git
    pkgs.gh
  ];
}

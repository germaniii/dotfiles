{
  description = "Dev Shell with Node.js and PHP";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs = { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          pkgs.nodejs_20
          pkgs.php82
        ];
        shellHook = ''
          echo "🧪 Dev shell with Node.js and PHP is ready"
        '';
      };
    };
}

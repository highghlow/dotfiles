sudo mkdir /etc/nixos/modules

cd nixos
sh setup-nixos.sh
cd ../

for nixfile in */config.nix; do
	echo ${nixfile}
	dirname=${nixfile%/config.nix}
	echo "Applying ${dirname}.nix"

	sudo ln -s ${PWD}/${nixfile} /etc/nixos/modules/${dirname}.nix
done

echo "Done applying modules"
echo "run \`nixos-rebuild switch\` to rebuild the system"

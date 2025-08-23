#!/bin/bash
set -e

echo "Starting Mizar installation..."

# 1. Update package lists and install dependencies
apt-get update && apt-get install -y wget tar

# 2. Download the official Mizar archive 
# URL for Mizar Version 8.1.15 with MML 5.94.1493
MIZAR_URL="https://mizar.uwb.edu.pl/~softadm/pub/system/i386-linux/mizar-8.1.15_5.94.1493-i386-linux.tar"
echo "Downloading Mizar from ${MIZAR_URL}..."
wget -q -O /tmp/mizar.tar "${MIZAR_URL}"

# 3. Create a temporary directory, extract the archive, and run the installer
echo "Extracting and installing Mizar..."
mkdir -p /tmp/mizar_install
tar -xvf /tmp/mizar.tar -C /tmp/mizar_install
cd /tmp/mizar_install

# Run the installer in non-interactive mode using the --default flag
./install.sh --default

# 4. Persist environment variables for all future terminal sessions
echo "Configuring environment variables..."
echo '' >> /etc/bash.bashrc
echo '# Set Mizar Environment Variables' >> /etc/bash.bashrc
echo 'export MIZFILES=/usr/local/share/mizar' >> /etc/bash.bashrc
echo 'export PATH=$PATH:/usr/local/bin' >> /etc/bash.bashrc

# 5. Clean up temporary files
echo "Cleaning up..."
cd /
rm -rf /tmp/mizar_install /tmp/mizar.tar

echo "Mizar installation complete."

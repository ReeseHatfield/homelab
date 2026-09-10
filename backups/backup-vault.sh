#!/bin/bash
VAULT_DIR="/home/$USER/vault"
# hope you have this configured as it documented
BACKUP_DEST="/mnt/backup-ssd/vault-archives"
DATE=$(date +%Y-%m-%d)

mkdir -p "$BACKUP_DEST"
echo "Initializing new vault backup..."

# tar my beloved
tar --zstd -cf "$BACKUP_DEST/vault-backup-$DATE.tar.zst" "$VAULT_DIR"

echo "Backup complete: vault-backup-$DATE.tar.zst created."
echo "Please double check this before trusting the backup"

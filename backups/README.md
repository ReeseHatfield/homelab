# Backups

Run all of this from `homelab` directory

## Drive Setup
Prepare an SSD to act as the backup target. Format with `ext4`. 

```bash
sudo mkfs.ext4 -L backup-ssd [TARGET PARTITION]
```

Create mount point and also configure `fstab` so it mounts on boot:
```bash
sudo mkdir -p /mnt/backup-ssd
```

Fstab:
```
UUID=[...] /mnt/backup-ssd ext4 defaults 0 2
```


Link `vault-backup.sh` to the `$PATH`
```bash
chmod +x backups/backup-vault.sh
sudo ln -s $(pwd)/backups/backup-vault.sh /usr/local/bin/backup-vault
```

You will also need to own the mountpoint:
```bash
sudo chown -R $USER:$USER /mnt/backup-ssd
```

Have a CRON job back up periodically (I do 1st of the month, at like 3:00am).

```bash
(crontab -l 2>/dev/null; echo "0 3 1 * * /usr/local/bin/backup-vault >> /home/rhatfield/forge/homelab/backup.log 2>&1") | crontab -
```

## Recovery:
To pull, you'll need to uncompress the tarball with tar + zstd
```bash
tar --zstd -xvf vault-backup-DATE.tar.zst
```

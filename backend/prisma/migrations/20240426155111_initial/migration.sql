-- CreateTable
CREATE TABLE "ModelRequest" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "request" TEXT NOT NULL,
    "performed_at" DATETIME NOT NULL
);

-- CreateTable
CREATE TABLE "ModelResponse" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "request_id" INTEGER NOT NULL,
    "started_at" DATETIME,
    "finished_at" DATETIME
);

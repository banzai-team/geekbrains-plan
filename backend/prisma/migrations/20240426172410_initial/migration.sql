-- CreateTable
CREATE TABLE "ModelRequest" (
    "id" SERIAL NOT NULL,
    "request" TEXT NOT NULL,
    "performed_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "ModelRequest_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "ModelResponse" (
    "id" SERIAL NOT NULL,
    "request_id" INTEGER NOT NULL,
    "started_at" TIMESTAMP(3),
    "finished_at" TIMESTAMP(3),

    CONSTRAINT "ModelResponse_pkey" PRIMARY KEY ("id")
);
